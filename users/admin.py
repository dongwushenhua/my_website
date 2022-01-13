from django.contrib import admin

# Register your models here.



# class MyAdminSite(admin.AdminSite):
# site_header = '动物园'
# site_title = '东吴神话的动物园'


# admin_site = MyAdminSite(name='management')


# class UserAdmin(admin.ModelAdmin):  # 一个固定的类，名字不能改
#     list_display = ['userName', 'passWord', 'createTime', 'phoneNumber', 'icon']  # 展示
#     list_per_page = 10  # 分页
#     ordering = ['-createTime']  # 减号为降序排序
#     # list_editable = ['userName']#直接可编辑，前提为display
#     # list_filter = ['userName']#过滤器
#     search_fields = ['userName']  # 按照用户名进行搜索
#     date_hierarchy = 'createTime'  # 按照日期进行分级
#
#
# admin.site.register(newUser)
# admin_site.register(newUser, UserAdmin)
