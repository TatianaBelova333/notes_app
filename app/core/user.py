import logging
from typing import Optional, Union

from fastapi import Depends, Request
from fastapi_users import (
    BaseUserManager, FastAPIUsers, IntegerIDMixin, InvalidPasswordException
)
from fastapi_users.authentication import (
    AuthenticationBackend, BearerTransport, JWTStrategy
)
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.core.constants import PASSWORD_LEN, TOKEN_LIFETIME
from app.core.db import get_async_session
from app.models.user import User
from app.schemas.user import UserCreate

logger = logging.getLogger()


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)


bearer_transport = BearerTransport(tokenUrl='auth/jwt/login')


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=settings.secret, lifetime_seconds=TOKEN_LIFETIME)


auth_backend = AuthenticationBackend(
    name='jwt',
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):

    async def validate_password(
        self,
        password: str,
        user: Union[UserCreate, User],
    ) -> None:
        if len(password) < PASSWORD_LEN:
            raise InvalidPasswordException(
                reason=(f'Пароль должен содержать не менее '
                        f'{PASSWORD_LEN} символов.')
            )
        if user.email in password:
            raise InvalidPasswordException(
                reason=f'Пароль не должен содержать {user.email}'
            )

    async def on_after_register(
            self, user: User, request: Optional[Request] = None
    ):
        logger.info(f'User {user.email} has been successfully registered.')


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user(active=True)
current_superuser = fastapi_users.current_user(active=True, superuser=True)
