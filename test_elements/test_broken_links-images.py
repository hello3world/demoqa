import requests


def test_broken_images(page):
    page = page
    page.goto("https://demoqa.com/broken")

    # Locate all images
    images = page.locator("img")
    for i in range(images.count()):
        img_url = images.nth(i).get_attribute("src")
        if img_url:
            # Make absolute URLs if needed
            if img_url.startswith("/"):
                img_url = "https://demoqa.com" + img_url

            # Check HTTP status code for each image
            try:
                response = requests.get(img_url, timeout=5)
                assert response.status_code == 200, f"Broken image found: {img_url}"
            except Exception as e:
                assert False, f"Error fetching image {img_url}: {e}"


def test_broken_links(page):
    page = page
    page.goto("https://demoqa.com/broken")

    # Locate all links
    links = page.locator("a")
    for i in range(links.count()):
        link_url = links.nth(i).get_attribute("href")
        if link_url:
            try:
                # Check HTTP status code for each link
                response = requests.get(link_url, timeout=5)
                assert response.status_code < 400, f"Broken link found: {link_url}"
            except Exception as e:
                assert False, f"Error fetching link {link_url}: {e}"
