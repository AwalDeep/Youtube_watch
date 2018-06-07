from django.views.generic.edit import FormView


from django.shortcuts import render

from youtubewatch.handlers.video_list_handler import VideoListHandler
from youtubewatch.forms import VideoSearch


class VideoList(FormView):
    template_name = 'youtubewatch/videolist.html'
    form_class = VideoSearch

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            query = request.POST['query']

            response = VideoListHandler().search_vid(query)

            return render(request, '', {'response': response})
    
