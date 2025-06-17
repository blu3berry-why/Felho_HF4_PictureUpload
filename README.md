# Picture Upload Django App

This Django application facilitates picture uploads, storage, and viewing. Users can upload pictures, view uploaded pictures, and delete pictures. Pictures are processed and stored in Azure Blob Storage.

## Table of Contents

- Overview
- Prerequisites
- Setup
- Models
- Views
- Templates
- Dependencies

---

## Overview

The Picture Upload Django app provides the following features:

- User authentication and management.
- Picture upload functionality with Azure Blob Storage integration.
- Picture viewing and deletion capabilities.

---

## Prerequisites

Before running the application, ensure you have the following prerequisites:

- Python 3.9+
- Django 4.2.11
- Azure Blob Storage account and access keys
- Azure account for configuration of Azure Blob Storage

---

## Setup

1. Clone the Repository:

git clone https://github.com/yourusername/picture-upload-django-app.git
cd picture-upload-django-app

2. Install Dependencies:

pip install -r requirements.txt

3. Configure Environment Variables:

Ensure you have set the following environment variables:

- SECRET_KEY: Django secret key for security.
- DEBUG: Set to True for debugging purposes.
- ALLOWED_HOSTS: List of allowed hosts for the Django application.
- AZURE_CONTAINER: Name of the Azure Blob Storage container.
- AZURE_ACCOUNT_NAME: Azure Storage account name.
- AZURE_ACCOUNT_KEY: Azure Storage account access key.

---

## Models

The Django app defines the following model:

### Post

- Fields: title, body, slug, date, banner, author
- Represents a post with a title, body content, publication date, banner image, and author information.

---

## Views

The Django app defines the following views:

- posts_lists: Displays a list of uploaded posts, sorted by date.
- post_page: Displays details of a specific post, including the image and post content.
- delete_page: Deletes a specific post.
- post_new: Allows authenticated users to upload a new post with an image.
- posts_sort_name: Sorts the list of posts by title.
- posts_sort_date: Sorts the list of posts by date.

---

## Templates

The Django app uses HTML templates for rendering views. Here's an overview of the main template:

### posts_list.html

- Displays a list of uploaded posts, sorted by date.
- Provides options to sort posts by date or name.
- Iterates over each post and displays its title, publication date, author, and body content.
- Links the title to the post detail page using the post's slug.

---

## Dependencies

The project uses the following dependencies:

- Django: Web framework for building web applications in Python.
- django-storages: Django library for working with various storage backends, including Azure Blob Storage.
