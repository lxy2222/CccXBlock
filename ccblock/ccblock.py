#coding=utf-8
import sys
import pkg_resources
from django.template import Context,Template
from xblock.core import XBlock
from xblock.fields import String,Integer
from xblock.fragment import Fragment
reload(sys)
sys.setdefaultencoding("utf-8")
class CccXBlock(XBlock):
    icon_class="video"
    '''
    Fields
    '''
    display_name = String(display_name="Display Name",
               default="cc player",
               scope=Scope.settings,
               help="This name appears in the top of the page")
    user_id = String(display_name="user id",
                     default=None,
                     scope=Scope.settings,
                     help="The user_id for your cc acount")
    video_id=String(display_name="video_id",
                    default=None,
                    scope=Scope.content,
                    help="The video_id for your video")
    width = Integer(display_name="width",default="800",scope=Scope.content,
                    help="The width of the video")
    height = Integer(display_name="height",default="450",scope=Scope.content,
                     help="The height of the video")
    def load_resource(self,resource_path):
        resource_content = pkg_resources.resource_string(__name__,resource_path)
        return unicode(resource_content)
    def render_template(self,template_path,context={}):
        template_str = self.load_resource(template_path)
        return Template(template_str).render(Context(context))
    def student_view(self,context=None):
        context = {
              'display_name':self.display_name,
              'user_id':self.user_id,
              'video_id':self.video_id,
              'width':self.width,
              'height':self.height,
        }
        html = self.render_template('static/html/ccblock_view.html', context)
        frag = Fragment(html)
        #frag.add_javascript(self.load_resource("static/js/youku_api.js"))
        frag.add_javascript(self.load_resource("static/js/src/ccblock_view.js"))
        frag.initialize_js('CccXBlockInitView')
        return frag
    def studio_view(self, context=None):
        
        context = {
            'display_name': self.display_name,
            'user_id':self.user_id,
            'video_id' : self.video_id,
            'width': self.width,
            'height':self.height,
             }
        html = self.render_template('static/html/ccblock_edit.html', context)
        frag = Fragment(html)
        frag.add_javascript(self.load_resource("static/js/src/ccblock_edit.js"))
        frag.initialize_js('CccXBlockInitStudio')
        return frag
    @XBlock.json_handler
    def save_cc(self, data, suffix=''):
        """
        The saving handler.
        """
        self.display_name = data['display_name']
        self.video_id = data['video_id']
        self.width = data['width']
        self.user_id = data['user_id']
        self.height = data['height']

        return {
            'result': 'success',
        }
    @XBlock.json_handler
    def get_params(self, data, suffix=''):
        '''called when cc init'''
        return {"video_id":self.video_id,
                "user_id":self.user_id,
                "width":self.width,
                "height":self.height,
                
                }
    @staticmethod
    def workbench_scenarios():
        return [
              ("ccblock", "<ccblock />")  #the name should be "<youku />"
        ]


