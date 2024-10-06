from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from .models import Profile, Addnewfield, Visitor

class ProfileFieldInline(admin.TabularInline):
    model = Addnewfield
    extra = 1

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'location')
    search_fields = ('name', 'email')
    inlines = [ProfileFieldInline]

@admin.register(Addnewfield)
class ProfileFieldAdmin(admin.ModelAdmin):
    list_display = ('profile', 'key')

