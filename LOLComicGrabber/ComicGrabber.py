import requests
import json
from bs4 import BeautifulSoup
import shutil
import os


class LOLComicGrabber():
    def __init__(self):
        self.issues_link = "https://universe-meeps.leagueoflegends.com/v1"
        self.base_link = "https://universe.leagueoflegends.com"

    def comic_json_link_builder(self, url, issue=None):
        """
        comic_json_link_build(url,issue) -> string

        Builds a link to the json that a comic is loaded from.

        :param url -- url inside json
        :param issue -- issue that you want to get json content for
                        (if applicable)
        """
        url = url.replace("en_US/comic", "en_us")
        if issue is None:
            full_url = f"https://universe-comics.leagueoflegends.com/comics{url}/index.json"
            # print(full_url)

        else:
            full_url = f"https://universe-comics.leagueoflegends.com/comics{url}/issue-{issue}/index.json"

        return full_url

    def objectify(self, link):
        """
        objectify(link) -> dictionary

        Makes a request to a given link and returns it in object form
        (Assumed that the response is in json)

        :param link -- link to a json response

        :returns content of the request to the link as an object
        """
        request = requests.get(link)
        content = request.content
        obj = json.loads(content)
        return obj

    def get_series(self):
        """
        get_series() -> dict

        Uses base link to get the series and information about series

        """
        series_response = {}
        obj = self.objectify(
            "https://universe-meeps.leagueoflegends.com/v1/en_us/comics/index.json")
        series_list = obj["sections"]["series"]["data"]
        for series in series_list:
            series_response[series["title"]] = series
        return series_response

    def get_series_issues(self, series):
        series_title = series["url"].split("/")[-1]
        series_link = f"https://universe-meeps.leagueoflegends.com/v1/en_us/comics/{series_title}/index.json"
        series_obj = self.objectify(series_link)
        return series_obj["issues"]

    def get_one_shots(self):
        """
        get_one_shots() -> dict

        Gets the one shots from the league comic site
        """
        one_shot_response = {}
        obj = self.objectify(
            "https://universe-meeps.leagueoflegends.com/v1/en_us/comics/index.json")
        series_list = obj["sections"]["one-shots"]["data"]
        for series in series_list:
            one_shot_response[series["title"]] = series

        return one_shot_response

    def get_issue(self, title):
        """
        get_issue(self, title) -> dict

        Gets the issue json info and returns it.

        :param title -- title of the comic issue (must be exact)

        :returns dictionary containing information on the issue

        """
        selection = self.get_one_shots()[title]
        selection_sub_url = selection["url"]
        full_url = self.comic_json_link_builder(selection_sub_url)
        issue_obj = self.objectify(full_url)
        # print(issue_obj)
        return issue_obj

    def get_issues(self, series):
        """
        get_issues(series) -> dict

        Gets the issues for a series in json/dict form.
        The dict will contain all the pages that we will use to download.

        :param series -- a dictionary for the series that is provided

        :returns issues within that series
        """
        issues = {}
        url = self.comic_json_link_builder(series["url"]).replace(
            "universe-comics", "universe-meeps").replace("comics/en_us",
                                                         "v1/en_us/comics")
        comic_issues_obj = self.objectify(url)
        for issue_index, issue in enumerate(comic_issues_obj["issues"]):
            issues[issue["title"]] = self.comic_json_link_builder(
                issue["url"])
        return issues

    def get_issue_pages(self, series=None, issue=0, is_series=True):
        """
        get_issue_pages(series, issue) -> (tuple)

        Returns the links and keys to the images in an issue

        :param series -- the series that the issue you want belongs to
        :param issue -- the issue that you want to pull images from

        :returns (page_img_links, key)
        """
        if is_series and series is not None and issue != 0:
            issue_num = f"Issue #{issue}"
            link_to_json_content = self.get_issues(
                self.get_series()[series])[issue_num]
            response_obj = self.objectify(link_to_json_content)
        else:
            # instead of a number this will be the title of the one-shot issue
            issue_num = issue
            response_obj = self.get_issue(issue)

        desktop_pages = response_obj["desktop-pages"]
        page_img_links = []
        for desktop_page in desktop_pages:
            if len(desktop_page) == 1:
                page_img_links.append(desktop_page[0]["uri"])
            else:
                for image in desktop_page:
                    page_img_links.append(image["uri"])

        return (page_img_links, issue_num)

    def download_pages(self, links, key, name):
        """
        download_pages(links, key, name) -> None

        Downloads pages of a given comic into a directory, zips the directory,
        and renames directory to a cbz to produce a comic book archive.

        :param links -- links to the images of the comic book pages
        :param key -- issue number (if applicable)
        :param name -- name of comic issue/series
        """
        key = key.replace(":", "")
        name = name.replace(":", "")
        dirname = f"{name} {key}" if key != name else name
        try:
            os.mkdir(dirname)
        except FileExistsError:
            pass
        os.chdir(dirname)
        for image in range(len(links)):
            # print()
            r = requests.get(links[image], stream=True)
            filename = \
                f'{name}_{key.replace("#","").replace(" ","") if key != name else ""}_{image if int(image)>9 else "0"+str(image)}.jpg'
            # print(filename)
            with open(filename, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
        os.chdir("..")
        shutil.make_archive(dirname, "zip", dirname)
        os.rename(f"{dirname}.zip", f"{dirname}.cbz")

    def download(self, series, issue=0, is_series=True):
        """
        download(series, issue=0, is_series=True) -> None

        Downloads according to whether or not the comic book desired is
        in a series or a one shot.

        :param series -- name of the series
        :param issue -- number of the issue.
                        If a one shot is selected,
                        enter the same value you did for the series arg
        :param is_series -- determines whether or not the desired comic
                            is in a series or not.
        """
        if is_series and issue != 0:
            self.download_pages(
                *(self.get_issue_pages(series, issue)), series)
        else:
            self.download_pages(
                *self.get_issue_pages(series, series, is_series=False), series)
