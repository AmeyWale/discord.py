"""
The MIT License (MIT)

Copyright (c) 2015-present Rapptz

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from typing import List, Literal, Optional, TypedDict, Union

from .snowflake import Snowflake
from .user import User
from .member import Member
from .channel import PrivacyLevel as PrivacyLevel

EventStatus = Literal[1, 2, 3, 4]
EntityType = Literal[1, 2, 3]


class _BaseGuildScheduledEventOptional(TypedDict, total=False):
    creator_id: Optional[Snowflake]
    description: str
    creator: User
    user_count: int


class _BaseGuildScheduledEvent(_BaseGuildScheduledEventOptional):
    id: Snowflake
    guild_id: Snowflake
    entity_id: Optional[Snowflake]
    name: str
    scheduled_start_time: str
    privacy_level: PrivacyLevel
    status: EventStatus
    image: Optional[str]


class _VoiceChannelScheduledEventOptional(_BaseGuildScheduledEvent, total=False):
    scheduled_end_time: Optional[str]


class _VoiceChannelScheduledEvent(_VoiceChannelScheduledEventOptional):
    channel_id: Snowflake
    entity_metadata: Literal[None]


class StageInstanceScheduledEvent(_VoiceChannelScheduledEvent):
    entity_type: Literal[1]


class VoiceScheduledEvent(_VoiceChannelScheduledEvent):
    entity_type: Literal[2]


class EntityMetadata(TypedDict):
    location: str


class ExternalScheduledEvent(_BaseGuildScheduledEvent):
    channel_id: Literal[None]
    entity_metadata: EntityMetadata
    scheduled_end_time: Optional[str]
    entity_type: Literal[3]


GuildScheduledEvent = Union[StageInstanceScheduledEvent, VoiceScheduledEvent, ExternalScheduledEvent]


class _WithUserCount(TypedDict):
    user_count: int


class _StageInstanceScheduledEventWithUserCount(StageInstanceScheduledEvent, _WithUserCount):
    ...


class _VoiceScheduledEventWithUserCount(VoiceScheduledEvent, _WithUserCount):
    ...


class _ExternalScheduledEventWithUserCount(ExternalScheduledEvent, _WithUserCount):
    ...


GuildScheduledEventWithUserCount = Union[
    _StageInstanceScheduledEventWithUserCount, _VoiceScheduledEventWithUserCount, _ExternalScheduledEventWithUserCount
]


class ScheduledEventUser(TypedDict):
    guild_scheduled_event_id: Snowflake
    user: User


class ScheduledEventUserWithMember(ScheduledEventUser):
    member: Member


ScheduledEventUsers = List[ScheduledEventUser]
ScheduledEventUsersWithMember = List[ScheduledEventUserWithMember]
