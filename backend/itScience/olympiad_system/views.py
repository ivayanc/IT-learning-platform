from django.shortcuts import render

# class VerifySolutionView(DetailView):
#     template_name = 'olympiad_system/verify.html'
    
#     queryset = Post.objects.all()

#     def get_object(self, queryset=None):
#         id_ = self.kwargs.get("id")
#         post = get_object_or_404(Post, pk=id_)
#         post.views += 1
#         post.save()
#         return post
    
#     def get_context_data(self, **kwargs):
                
#         context = super().get_context_data(**kwargs)
#         context['latest_posts'] = Post.objects.all().filter(category=context['object'].category)[:3]
#         context['is_favorite'] = False
#         if len(self.get_object().favorite.filter(id = self.request.user.pk)):
#             context['is_favorite'] = True

#         return context