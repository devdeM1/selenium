def find_matching_images(dynamic_content_page, max_attempts=10):
    images = []
    for _ in range(max_attempts):
        dynamic_content_page.reload()
        images = dynamic_content_page.get_user_images()
        if len(set(images)) < len(images):
            return True
    return False