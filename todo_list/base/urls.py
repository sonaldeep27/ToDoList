from django.urls import path
from .views import TaskDelete, TaskList, TaskDetail, TaskCreate, TaskUpdate, CustomLogin, CustomLogout, CustomRegister

urlpatterns = [
    path('login/', CustomLogin.as_view(), name='login'),
    path('logout/', CustomLogout.as_view(), name='logout'),
    path('register/', CustomRegister.as_view(), name='register'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>', TaskDelete.as_view(), name='task-delete'),
]
