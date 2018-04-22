"""
XBlock which embeds a Virtual Reality Video
"""

from xblock.core import XBlock
from xblock.fields import Scope, String
from xblock.fragment import Fragment
from xblockutils.resources import ResourceLoader
from xblockutils.studio_editable import StudioEditableXBlockMixin


def _(text):
    """
    Dummy `gettext` replacement to make string extraction tools
    scrape strings marked for translation
    """
    return text

loader = ResourceLoader(__name__)


class VRBlock(StudioEditableXBlockMixin, XBlock):
    """
    An XBlock for embedding Virtual Reality Videos
    """
    display_name = String(default=_("Virtual Reality"))
    icon_class = 'video'

    title = String(
        display_name=_("Title"),
        help=_("Video Title"),
        default=_("Video Title"),
        scope=Scope.content
    )
    description = String(
        display_name=_("Description"),
        help=_("Video Description"),
        default=_("Video Description"),
        scope=Scope.content
    )
    embed_code = String(
        display_name=_("Embed Code"),
        help=_("URL for Vimeo 360 URL"),
        default="https://player.vimeo.com/video/207466022",
        scope=Scope.content
    )
    highres_url = String(
        display_name=_("High Resolution Video URL"),
        help=_("URL to high resolution video"),
        default="",
        scope=Scope.content
    )
    lowres_url = String(
        display_name=_("Low Resolution Video URL"),
        help=_("URL to low resolution video"),
        default="",
        scope=Scope.content
    )

    editable_fields = (
        "title",
        "description",
        "embed_code",
        "highres_url",
        "lowres_url"
    )

    def student_view(self, context=None):
        """
        View to be shown to students in the LMS.
        """
        context = {
            u"title": self.title,
            u"description": self.description,
            u"embed_code": self.embed_code
        }
        fragment = Fragment()
        fragment.add_content(
            loader.render_template("templates/vr.html", context)
        )
        fragment.add_css_url(
            self.runtime.local_resource_url(self, "public/css/vr.css")
        )
        self.runtime.publish(self, 'progress', {})
        return fragment

    def student_view_data(self, context=None):
        """
        Returns a JSON representation of the video.
        """
        return {
            'title': self.title,
            'description': self.description,
            'embed_code': self.embed_code,
            'highres_url': self.highres_url,
            'lowres_url': self.lowres_url,
        }
