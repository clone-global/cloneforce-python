# V1

## Clones

Types:

```python
from cloneforce.types.v1 import CloneListResponse
```

Methods:

- <code title="get /api/v1/clones">client.v1.clones.<a href="./src/cloneforce/resources/v1/clones/clones.py">list</a>() -> <a href="./src/cloneforce/types/v1/clone_list_response.py">CloneListResponse</a></code>

### Profile

Types:

```python
from cloneforce.types.v1.clones import CloneHeadshot, CloneProfile
```

Methods:

- <code title="get /api/v1/clones/{cloneId}/profile">client.v1.clones.profile.<a href="./src/cloneforce/resources/v1/clones/profile.py">list</a>(clone_id) -> <a href="./src/cloneforce/types/v1/clones/clone_profile.py">CloneProfile</a></code>
- <code title="patch /api/v1/clones/{cloneId}/profile">client.v1.clones.profile.<a href="./src/cloneforce/resources/v1/clones/profile.py">patch_all</a>(clone_id, \*\*<a href="src/cloneforce/types/v1/clones/profile_patch_all_params.py">params</a>) -> <a href="./src/cloneforce/types/v1/clones/clone_profile.py">CloneProfile</a></code>

### Voice

Types:

```python
from cloneforce.types.v1.clones import GenerateRequest, GenerationStatus
```

Methods:

- <code title="post /api/v1/clones/{cloneId}/voice/generate">client.v1.clones.voice.<a href="./src/cloneforce/resources/v1/clones/voice.py">generate</a>(clone_id, \*\*<a href="src/cloneforce/types/v1/clones/voice_generate_params.py">params</a>) -> <a href="./src/cloneforce/types/v1/clones/generation_status.py">GenerationStatus</a></code>

### Headshot

Methods:

- <code title="post /api/v1/clones/{cloneId}/headshot/generate">client.v1.clones.headshot.<a href="./src/cloneforce/resources/v1/clones/headshot.py">generate</a>(clone_id, \*\*<a href="src/cloneforce/types/v1/clones/headshot_generate_params.py">params</a>) -> <a href="./src/cloneforce/types/v1/clones/generation_status.py">GenerationStatus</a></code>

### Skills

Types:

```python
from cloneforce.types.v1.clones import SkillSummary, SkillListResponse, SkillDeleteResponse
```

Methods:

- <code title="post /api/v1/clones/{cloneId}/skills">client.v1.clones.skills.<a href="./src/cloneforce/resources/v1/clones/skills/skills.py">create</a>(clone_id, \*\*<a href="src/cloneforce/types/v1/clones/skill_create_params.py">params</a>) -> <a href="./src/cloneforce/types/v1/clones/skill_summary.py">SkillSummary</a></code>
- <code title="patch /api/v1/clones/{cloneId}/skills/{skillName}">client.v1.clones.skills.<a href="./src/cloneforce/resources/v1/clones/skills/skills.py">update</a>(skill_name, \*, clone_id, \*\*<a href="src/cloneforce/types/v1/clones/skill_update_params.py">params</a>) -> <a href="./src/cloneforce/types/v1/clones/skill_summary.py">SkillSummary</a></code>
- <code title="get /api/v1/clones/{cloneId}/skills">client.v1.clones.skills.<a href="./src/cloneforce/resources/v1/clones/skills/skills.py">list</a>(clone_id, \*\*<a href="src/cloneforce/types/v1/clones/skill_list_params.py">params</a>) -> <a href="./src/cloneforce/types/v1/clones/skill_list_response.py">SkillListResponse</a></code>
- <code title="delete /api/v1/clones/{cloneId}/skills/{skillName}">client.v1.clones.skills.<a href="./src/cloneforce/resources/v1/clones/skills/skills.py">delete</a>(skill_name, \*, clone_id) -> <a href="./src/cloneforce/types/v1/clones/skill_delete_response.py">SkillDeleteResponse</a></code>

#### Connections

Types:

```python
from cloneforce.types.v1.clones.skills import SkillConnectionInfo, ConnectionListResponse
```

Methods:

- <code title="put /api/v1/clones/{cloneId}/skills/{skillName}/connections/{settingName}">client.v1.clones.skills.connections.<a href="./src/cloneforce/resources/v1/clones/skills/connections.py">update</a>(setting_name, \*, clone_id, skill_name, \*\*<a href="src/cloneforce/types/v1/clones/skills/connection_update_params.py">params</a>) -> <a href="./src/cloneforce/types/v1/clones/skills/skill_connection_info.py">SkillConnectionInfo</a></code>
- <code title="get /api/v1/clones/{cloneId}/skills/{skillName}/connections">client.v1.clones.skills.connections.<a href="./src/cloneforce/resources/v1/clones/skills/connections.py">list</a>(skill_name, \*, clone_id) -> <a href="./src/cloneforce/types/v1/clones/skills/connection_list_response.py">ConnectionListResponse</a></code>

### Tasks

Types:

```python
from cloneforce.types.v1.clones import (
    TaskRecurrence,
    TaskSummary,
    TaskListResponse,
    TaskDeleteResponse,
)
```

Methods:

- <code title="post /api/v1/clones/{cloneId}/tasks">client.v1.clones.tasks.<a href="./src/cloneforce/resources/v1/clones/tasks.py">create</a>(clone_id, \*\*<a href="src/cloneforce/types/v1/clones/task_create_params.py">params</a>) -> <a href="./src/cloneforce/types/v1/clones/task_summary.py">TaskSummary</a></code>
- <code title="get /api/v1/clones/{cloneId}/tasks/{taskId}">client.v1.clones.tasks.<a href="./src/cloneforce/resources/v1/clones/tasks.py">retrieve</a>(task_id, \*, clone_id) -> <a href="./src/cloneforce/types/v1/clones/task_summary.py">TaskSummary</a></code>
- <code title="patch /api/v1/clones/{cloneId}/tasks/{taskId}">client.v1.clones.tasks.<a href="./src/cloneforce/resources/v1/clones/tasks.py">update</a>(task_id, \*, clone_id, \*\*<a href="src/cloneforce/types/v1/clones/task_update_params.py">params</a>) -> <a href="./src/cloneforce/types/v1/clones/task_summary.py">TaskSummary</a></code>
- <code title="get /api/v1/clones/{cloneId}/tasks">client.v1.clones.tasks.<a href="./src/cloneforce/resources/v1/clones/tasks.py">list</a>(clone_id, \*\*<a href="src/cloneforce/types/v1/clones/task_list_params.py">params</a>) -> <a href="./src/cloneforce/types/v1/clones/task_list_response.py">TaskListResponse</a></code>
- <code title="delete /api/v1/clones/{cloneId}/tasks/{taskId}">client.v1.clones.tasks.<a href="./src/cloneforce/resources/v1/clones/tasks.py">delete</a>(task_id, \*, clone_id) -> <a href="./src/cloneforce/types/v1/clones/task_delete_response.py">TaskDeleteResponse</a></code>

### Files

Types:

```python
from cloneforce.types.v1.clones import KBFileSummary, FileListResponse, FileDeleteResponse
```

Methods:

- <code title="post /api/v1/clones/{cloneId}/files">client.v1.clones.files.<a href="./src/cloneforce/resources/v1/clones/files.py">create</a>(clone_id, \*\*<a href="src/cloneforce/types/v1/clones/file_create_params.py">params</a>) -> <a href="./src/cloneforce/types/v1/clones/kb_file_summary.py">KBFileSummary</a></code>
- <code title="get /api/v1/clones/{cloneId}/files/{fileId}">client.v1.clones.files.<a href="./src/cloneforce/resources/v1/clones/files.py">retrieve</a>(file_id, \*, clone_id) -> <a href="./src/cloneforce/types/v1/clones/kb_file_summary.py">KBFileSummary</a></code>
- <code title="get /api/v1/clones/{cloneId}/files">client.v1.clones.files.<a href="./src/cloneforce/resources/v1/clones/files.py">list</a>(clone_id) -> <a href="./src/cloneforce/types/v1/clones/file_list_response.py">FileListResponse</a></code>
- <code title="delete /api/v1/clones/{cloneId}/files/{fileId}">client.v1.clones.files.<a href="./src/cloneforce/resources/v1/clones/files.py">delete</a>(file_id, \*, clone_id) -> <a href="./src/cloneforce/types/v1/clones/file_delete_response.py">FileDeleteResponse</a></code>

### Gallery

Types:

```python
from cloneforce.types.v1.clones import (
    GalleryItemSummary,
    GalleryListResponse,
    GalleryDeleteResponse,
)
```

Methods:

- <code title="post /api/v1/clones/{cloneId}/gallery">client.v1.clones.gallery.<a href="./src/cloneforce/resources/v1/clones/gallery.py">create</a>(clone_id, \*\*<a href="src/cloneforce/types/v1/clones/gallery_create_params.py">params</a>) -> <a href="./src/cloneforce/types/v1/clones/gallery_item_summary.py">GalleryItemSummary</a></code>
- <code title="get /api/v1/clones/{cloneId}/gallery/{itemId}">client.v1.clones.gallery.<a href="./src/cloneforce/resources/v1/clones/gallery.py">retrieve</a>(item_id, \*, clone_id) -> <a href="./src/cloneforce/types/v1/clones/gallery_item_summary.py">GalleryItemSummary</a></code>
- <code title="get /api/v1/clones/{cloneId}/gallery">client.v1.clones.gallery.<a href="./src/cloneforce/resources/v1/clones/gallery.py">list</a>(clone_id, \*\*<a href="src/cloneforce/types/v1/clones/gallery_list_params.py">params</a>) -> <a href="./src/cloneforce/types/v1/clones/gallery_list_response.py">GalleryListResponse</a></code>
- <code title="delete /api/v1/clones/{cloneId}/gallery/{itemId}">client.v1.clones.gallery.<a href="./src/cloneforce/resources/v1/clones/gallery.py">delete</a>(item_id, \*, clone_id) -> <a href="./src/cloneforce/types/v1/clones/gallery_delete_response.py">GalleryDeleteResponse</a></code>

### Integrations

Types:

```python
from cloneforce.types.v1.clones import (
    IntegrationSummary,
    IntegrationListResponse,
    IntegrationDeleteResponse,
    IntegrationPhoneResponse,
    IntegrationRetrieveSetupResponse,
)
```

Methods:

- <code title="get /api/v1/clones/{cloneId}/integrations/{integrationId}">client.v1.clones.integrations.<a href="./src/cloneforce/resources/v1/clones/integrations/integrations.py">retrieve</a>(integration_id, \*, clone_id) -> <a href="./src/cloneforce/types/v1/clones/integration_summary.py">IntegrationSummary</a></code>
- <code title="get /api/v1/clones/{cloneId}/integrations">client.v1.clones.integrations.<a href="./src/cloneforce/resources/v1/clones/integrations/integrations.py">list</a>(clone_id, \*\*<a href="src/cloneforce/types/v1/clones/integration_list_params.py">params</a>) -> <a href="./src/cloneforce/types/v1/clones/integration_list_response.py">IntegrationListResponse</a></code>
- <code title="delete /api/v1/clones/{cloneId}/integrations/{integrationId}">client.v1.clones.integrations.<a href="./src/cloneforce/resources/v1/clones/integrations/integrations.py">delete</a>(integration_id, \*, clone_id) -> <a href="./src/cloneforce/types/v1/clones/integration_delete_response.py">IntegrationDeleteResponse</a></code>
- <code title="post /api/v1/clones/{cloneId}/integrations/phone">client.v1.clones.integrations.<a href="./src/cloneforce/resources/v1/clones/integrations/integrations.py">phone</a>(clone_id, \*\*<a href="src/cloneforce/types/v1/clones/integration_phone_params.py">params</a>) -> <a href="./src/cloneforce/types/v1/clones/integration_phone_response.py">IntegrationPhoneResponse</a></code>
- <code title="get /api/v1/clones/{cloneId}/integrations/{type}/setup">client.v1.clones.integrations.<a href="./src/cloneforce/resources/v1/clones/integrations/integrations.py">retrieve_setup</a>(type, \*, clone_id) -> <a href="./src/cloneforce/types/v1/clones/integration_retrieve_setup_response.py">IntegrationRetrieveSetupResponse</a></code>

#### Slack

Types:

```python
from cloneforce.types.v1.clones.integrations import SlackIntegration
```

Methods:

- <code title="post /api/v1/clones/{cloneId}/integrations/slack">client.v1.clones.integrations.slack.<a href="./src/cloneforce/resources/v1/clones/integrations/slack.py">create</a>(clone_id) -> <a href="./src/cloneforce/types/v1/clones/integrations/slack_integration.py">SlackIntegration</a></code>
- <code title="patch /api/v1/clones/{cloneId}/integrations/slack/{integrationId}">client.v1.clones.integrations.slack.<a href="./src/cloneforce/resources/v1/clones/integrations/slack.py">update</a>(integration_id, \*, clone_id, \*\*<a href="src/cloneforce/types/v1/clones/integrations/slack_update_params.py">params</a>) -> <a href="./src/cloneforce/types/v1/clones/integrations/slack_integration.py">SlackIntegration</a></code>

#### Msteams

Types:

```python
from cloneforce.types.v1.clones.integrations import MsTeamsTeamRef, MsteamTeamsResponse
```

Methods:

- <code title="post /api/v1/clones/{cloneId}/integrations/msteams/{integrationId}/teams">client.v1.clones.integrations.msteams.<a href="./src/cloneforce/resources/v1/clones/integrations/msteams.py">teams</a>(integration_id, \*, clone_id, \*\*<a href="src/cloneforce/types/v1/clones/integrations/msteam_teams_params.py">params</a>) -> <a href="./src/cloneforce/types/v1/clones/integrations/msteam_teams_response.py">MsteamTeamsResponse</a></code>

### Activity

Types:

```python
from cloneforce.types.v1.clones import (
    ActivityRetrieveResponse,
    ActivityListResponse,
    ActivityDeleteResponse,
)
```

Methods:

- <code title="get /api/v1/clones/{cloneId}/activity/{activityId}">client.v1.clones.activity.<a href="./src/cloneforce/resources/v1/clones/activity.py">retrieve</a>(activity_id, \*, clone_id) -> <a href="./src/cloneforce/types/v1/clones/activity_retrieve_response.py">ActivityRetrieveResponse</a></code>
- <code title="get /api/v1/clones/{cloneId}/activity">client.v1.clones.activity.<a href="./src/cloneforce/resources/v1/clones/activity.py">list</a>(clone_id) -> <a href="./src/cloneforce/types/v1/clones/activity_list_response.py">ActivityListResponse</a></code>
- <code title="delete /api/v1/clones/{cloneId}/activity/{activityId}">client.v1.clones.activity.<a href="./src/cloneforce/resources/v1/clones/activity.py">delete</a>(activity_id, \*, clone_id) -> <a href="./src/cloneforce/types/v1/clones/activity_delete_response.py">ActivityDeleteResponse</a></code>

## Skills

Types:

```python
from cloneforce.types.v1 import SkillRetrieveResponse, SkillSearchResponse
```

Methods:

- <code title="get /api/v1/skills/{skillId}">client.v1.skills.<a href="./src/cloneforce/resources/v1/skills.py">retrieve</a>(skill_id, \*\*<a href="src/cloneforce/types/v1/skill_retrieve_params.py">params</a>) -> <a href="./src/cloneforce/types/v1/skill_retrieve_response.py">SkillRetrieveResponse</a></code>
- <code title="get /api/v1/skills/search">client.v1.skills.<a href="./src/cloneforce/resources/v1/skills.py">search</a>(\*\*<a href="src/cloneforce/types/v1/skill_search_params.py">params</a>) -> <a href="./src/cloneforce/types/v1/skill_search_response.py">SkillSearchResponse</a></code>

## Integrations

### Phone

Types:

```python
from cloneforce.types.v1.integrations import PhoneListAvailableResponse
```

Methods:

- <code title="get /api/v1/integrations/phone/available">client.v1.integrations.phone.<a href="./src/cloneforce/resources/v1/integrations/phone.py">list_available</a>(\*\*<a href="src/cloneforce/types/v1/integrations/phone_list_available_params.py">params</a>) -> <a href="./src/cloneforce/types/v1/integrations/phone_list_available_response.py">PhoneListAvailableResponse</a></code>

## Connections

Types:

```python
from cloneforce.types.v1 import (
    ConnectionDetail,
    ConnectionStatus,
    OAuthProvision,
    ConnectionListResponse,
    ConnectionDeleteResponse,
)
```

Methods:

- <code title="post /api/v1/connections">client.v1.connections.<a href="./src/cloneforce/resources/v1/connections.py">create</a>(\*\*<a href="src/cloneforce/types/v1/connection_create_params.py">params</a>) -> <a href="./src/cloneforce/types/v1/connection_detail.py">ConnectionDetail</a></code>
- <code title="get /api/v1/connections/{connectionId}">client.v1.connections.<a href="./src/cloneforce/resources/v1/connections.py">retrieve</a>(connection_id) -> <a href="./src/cloneforce/types/v1/connection_detail.py">ConnectionDetail</a></code>
- <code title="patch /api/v1/connections/{connectionId}">client.v1.connections.<a href="./src/cloneforce/resources/v1/connections.py">update</a>(connection_id, \*\*<a href="src/cloneforce/types/v1/connection_update_params.py">params</a>) -> <a href="./src/cloneforce/types/v1/connection_detail.py">ConnectionDetail</a></code>
- <code title="get /api/v1/connections">client.v1.connections.<a href="./src/cloneforce/resources/v1/connections.py">list</a>(\*\*<a href="src/cloneforce/types/v1/connection_list_params.py">params</a>) -> <a href="./src/cloneforce/types/v1/connection_list_response.py">ConnectionListResponse</a></code>
- <code title="delete /api/v1/connections/{connectionId}">client.v1.connections.<a href="./src/cloneforce/resources/v1/connections.py">delete</a>(connection_id) -> <a href="./src/cloneforce/types/v1/connection_delete_response.py">ConnectionDeleteResponse</a></code>
- <code title="post /api/v1/connections/oauth">client.v1.connections.<a href="./src/cloneforce/resources/v1/connections.py">create_oauth</a>(\*\*<a href="src/cloneforce/types/v1/connection_create_oauth_params.py">params</a>) -> <a href="./src/cloneforce/types/v1/oauth_provision.py">OAuthProvision</a></code>
- <code title="get /api/v1/connections/{connectionId}/status">client.v1.connections.<a href="./src/cloneforce/resources/v1/connections.py">get_status</a>(connection_id) -> <a href="./src/cloneforce/types/v1/connection_status.py">ConnectionStatus</a></code>
- <code title="post /api/v1/connections/{connectionId}/refresh">client.v1.connections.<a href="./src/cloneforce/resources/v1/connections.py">refresh</a>(connection_id) -> <a href="./src/cloneforce/types/v1/connection_status.py">ConnectionStatus</a></code>
- <code title="post /api/v1/connections/{connectionId}/reprovision">client.v1.connections.<a href="./src/cloneforce/resources/v1/connections.py">reprovision_oauth</a>(connection_id) -> <a href="./src/cloneforce/types/v1/oauth_provision.py">OAuthProvision</a></code>
