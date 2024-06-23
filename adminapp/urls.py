from django.urls import path, include
from adminapp import views

urlpatterns = [
    path('adminpage/', views.adminpage, name="adminpage"),
    path('emppage/', views.emppage, name="emppage"),
    path('saveemployee/', views.saveemployee, name="saveemployee"),
    path('empdisplay/', views.empdisplay, name="empdisplay"),
    path('designation/', views.designation, name="designation"),
    path('savepost/', views.savepost, name="savepost"),
    path('postdisplay/', views.postdisplay, name="postdisplay"),
    path('farmerpage/', views.farmerpage, name="farmerpage"),
    path('savefarmer/', views.savefarmer, name="savefarmer"),
    path('editemp/<int:dataid>/', views.editemp, name="editemp"),
    path('empupdate/<int:dataid>/', views.empupdate, name="empupdate"),
    path('empdelete/<int:dataid>/', views.empdelete, name="empdelete"),
    path('loginpage/', views.loginpage, name="loginpage"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),
    path('empdata/', views.empdata, name="empdata"),
    path('dispfarmer/', views.dispfarmer, name="dispfarmer"),
    path('editfarmer/<int:dataid>/', views.editfarmer, name="editfarmer"),
    path('farmerupdate/<int:dataid>/', views.farmerupdate, name="farmerupdate"),
    path('farmerdelete/<int:dataid>/', views.farmerdelete, name="farmerdelete"),
    path('attendance/', views.attendance, name="attendance"),
    path('saveatn/', views.saveatn, name="saveatn"),
    path('viewatn/', views.viewatn, name="viewatn"),
    path('editpost/<int:dataid>/', views.editpost, name="editpost"),
    path('postupdate/<int:dataid>/', views.postupdate, name="postupdate"),
    path('postdelete/<int:dataid>/', views.postdelete, name="postdelete"),
    path('viewbydate/', views.viewbydate, name="viewbydate"),
    path('viewbyemp/', views.viewbyemp, name="viewbyemp"),
    path('viewallatn/', views.viewallatn, name="viewallatn"),
    path('viewfarmer/', views.viewfarmer, name="viewfarmer"),
    path('atndelete/<int:dataid>/', views.atndelete, name="atndelete"),
    path('imgupload/', views.imgupload, name="imgupload"),
    path('saveimg/', views.saveimg, name="saveimg"),
    path('viewimage/', views.viewimage, name="viewimage"),
    path('dltimg/<int:dataid>/', views.dltimg, name="dltimg"),
    path('orders/', views.orders, name="orders"),
    path('adminsales/', views.adminsales, name="adminsales"),
    path('milkrecord/', views.milkrecord, name="milkrecord"),
    path('viewmsg/', views.viewmsg, name="viewmsg"),
    path('reply/<int:dataid>/', views.reply, name="reply"),
    path('send-email/<int:dataid>/', views.send_email, name='send_email'),
   ]
