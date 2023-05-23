## All Can Use This
## Example

### Basic Usage

``` python
from instagrapi import Client

cl = Client()
cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)

user_id = cl.user_id_from_username("adw0rd")
medias = cl.user_medias(user_id, 20)
```

<details>
    <summary>The full example</summary>

```python
from instagrapi import Client
from instagrapi.types import Location, StoryMention, StoryLocation, StoryLink, StoryHashtag

cl = Client()
cl.login(USERNAME, PASSWORD, verification_code="<2FA CODE HERE>")

media_path = cl.video_download(
    cl.media_pk_from_url('https://www.instagram.com/p/CGgDsi7JQdS/')
)
adw0rd = cl.user_info_by_username('adw0rd')
loc = cl.location_complete(Location(name='Test', lat=42.0, lng=42.0))
ht = cl.hashtag_info('dhbastards')

cl.video_upload_to_story(
    media_path,
    "Credits @adw0rd",
    mentions=[StoryMention(user=adw0rd, x=0.49892962, y=0.703125, width=0.8333333333333334, height=0.125)],
    locations=[StoryLocation(location=loc, x=0.33, y=0.22, width=0.4, height=0.7)],
    links=[StoryLink(webUri='https://github.com/adw0rd/instagrapi')],
    hashtags=[StoryHashtag(hashtag=ht, x=0.23, y=0.32, width=0.5, height=0.22)],
)
```
</details>

## Documentation

* [Index](https://adw0rd.github.io/instagrapi/)
* [Getting Started](https://adw0rd.github.io/instagrapi/getting-started.html)
* [Usage Guide](https://adw0rd.github.io/instagrapi/usage-guide/fundamentals.html)
* [Interactions](https://adw0rd.github.io/instagrapi/usage-guide/interactions.html)
  * [`Media`](https://adw0rd.github.io/instagrapi/usage-guide/media.html) - Publication (also called post): Photo, Video, Album, IGTV and Reels
  * [`Resource`](https://adw0rd.github.io/instagrapi/usage-guide/media.html) - Part of Media (for albums)
  * [`MediaOembed`](https://adw0rd.github.io/instagrapi/usage-guide/media.html) - Short version of Media
  * [`Account`](https://adw0rd.github.io/instagrapi/usage-guide/account.html) - Full private info for your account (e.g. email, phone_number)
  * [`User`](https://adw0rd.github.io/instagrapi/usage-guide/user.html) - Full public user data
  * [`UserShort`](https://adw0rd.github.io/instagrapi/usage-guide/user.html) - Short public user data (used in Usertag, Comment, Media, Direct Message)
  * [`Usertag`](https://adw0rd.github.io/instagrapi/usage-guide/user.html) - Tag user in Media (coordinates + UserShort)
  * [`Location`](https://adw0rd.github.io/instagrapi/usage-guide/location.html) - GEO location (GEO coordinates, name, address)
  * [`Hashtag`](https://adw0rd.github.io/instagrapi/usage-guide/hashtag.html) - Hashtag object (id, name, picture)
  * [`Collection`](https://adw0rd.github.io/instagrapi/usage-guide/collection.html) - Collection of medias (name, picture and list of medias)
  * [`Comment`](https://adw0rd.github.io/instagrapi/usage-guide/comment.html) - Comments to Media
  * [`Story`](https://adw0rd.github.io/instagrapi/usage-guide/story.html) - Story
  * [`StoryLink`](https://adw0rd.github.io/instagrapi/usage-guide/story.html) - Link (Swipe up)
  * [`StoryLocation`](https://adw0rd.github.io/instagrapi/usage-guide/story.html) - Tag Location in Story (as sticker)
  * [`StoryMention`](https://adw0rd.github.io/instagrapi/usage-guide/story.html) - Mention users in Story (user, coordinates and dimensions)
  * [`StoryHashtag`](https://adw0rd.github.io/instagrapi/usage-guide/story.html) - Hashtag for story (as sticker)
  * [`StorySticker`](https://adw0rd.github.io/instagrapi/usage-guide/story.html) - Tag sticker to story (for example from giphy)
  * [`StoryBuild`](https://adw0rd.github.io/instagrapi/usage-guide/story.html) - [StoryBuilder](/instagrapi/story.py) return path to photo/video and mention co-ordinates
  * [`DirectThread`](https://adw0rd.github.io/instagrapi/usage-guide/direct.html) - Thread (topic) with messages in Direct Message
  * [`DirectMessage`](https://adw0rd.github.io/instagrapi/usage-guide/direct.html) - Message in Direct Message
  * [`Insight`](https://adw0rd.github.io/instagrapi/usage-guide/insight.html) - Insights for a post
* [Development Guide](https://adw0rd.github.io/instagrapi/development-guide.html)
* [Handle Exceptions](https://adw0rd.github.io/instagrapi/usage-guide/handle_exception.html)
* [Challenge Resolver](https://adw0rd.github.io/instagrapi/usage-guide/challenge_resolver.html)
* [Exceptions](https://adw0rd.github.io/instagrapi/exceptions.html)
