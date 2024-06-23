from django.urls import path, include
from empapp import views
urlpatterns = [
    path('emploginpage/', views.emploginpage, name="emploginpage"),
    path('mchome/', views.mchome, name="mchome"),
    path('saleshome/', views.saleshome, name="saleshome"),
    path('employeelogin/', views.employeelogin, name="employeelogin"),
    path('addproduct/', views.addproduct, name="addproduct"),
    path('saveproduct/', views.saveproduct, name="saveproduct"),
    path('dispproduct/', views.dispproduct, name="dispproduct"),
    path('editproduct/<int:dataid>/', views.editproduct, name="editproduct"),
    path('updateproduct/<int:dataid>/', views.updateproduct, name="updateproduct"),
    path('deleteproduct/<int:dataid>/', views.deleteproduct, name="deleteproduct"),
    path('customer/', views.customer, name="customer"),
    path('savecustomer/', views.savecustomer, name="savecustomer"),
    path('sales/', views.sales, name="sales"),
    path('savesales/', views.savesales, name="savesales"),
    path('viewsalesrecord/', views.viewsalesrecord, name="viewsalesrecord"),
    path('emplogout/', views.emplogout, name="emplogout"),
    path('salebill/', views.salebill, name="salebill"),
    path('billview/', views.billview, name="billview"),
    path('savebill/', views.savebill, name="savebill"),
    path('addpricechart/', views.addpricechart, name="addpricechart"),
    path('savepc/', views.savepc, name="savepc"),
    path('milkcollection/', views.milkcollection, name="milkcollection"),
    path('savemc/', views.savemc, name="savemc"),
    path('milktest/', views.milktest, name="milktest"),
    path('savetest/', views.savetest, name="savetest"),
    path('savetotal/', views.savetotal, name="savetotal"),
    path('totalbill/', views.totalbill, name="totalbill"),
    path('customerview/', views.customerview, name="customerview"),
    path('editcustomer/<int:dataid>/', views.editcustomer, name="editcustomer"),
    path('dltcustomer/<int:dataid>/', views.dltcustomer, name="dltcustomer"),
    path('updatecustomer/<int:dataid>/', views.updatecustomer, name="updatecustomer"),
    path('milkrecordview/', views.milkrecordview, name="milkrecordview"),
    path('milkview/', views.milkview, name="milkview"),
    path('viewbydatemilk/', views.viewbydatemilk, name="viewbydatemilk"),
    path('viewbyfarmer/', views.viewbyfarmer, name="viewbyfarmer"),
    path('viewsalesdate/', views.viewsalesdate, name="viewsalesdate"),
    path('viewdaysales/', views.viewdaysales, name="viewdaysales"),
    path('viewsalesday/', views.viewsalesday, name="viewsalesday"),
    path('viewpc/', views.viewpc, name="viewpc"),
    path('pcdlt/<int:dataid>/', views.pcdlt, name="pcdlt"),
    path('salerange/', views.salerange, name="salerange"),
    path('incomerange/', views.incomerange, name="incomerange"),
    path('orderspage/', views.orderspage, name="orderspage"),
    path('savestatus/<int:dataid>/', views.savestatus, name="savestatus"),
    path('amount/', views.amount, name="amount"),
    path('calculateamount/', views.calculateamount, name="calculateamount")

]