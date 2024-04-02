#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/24 15:46
# @Description : 【某某系统项目】-【登录】-【界面自动化测试用例】
# @Author  : Simon
# @File    : CaseForMarketingLogin.py
# @Software: IntelliJ IDEA


import time
import logging
import allure
from playwright.sync_api import Page, sync_playwright, Playwright
from src.config.constant.env_url import TEST_ENV


logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class CaseForMarketingLogin():
    @allure.description("""【某某系统项目】-【登录】-【界面自动化测试用例】""")
    def test_example(playwright: Playwright) -> None:
        logger.info("【某某系统项目】-【登录】-【界面自动化测试用例】-【开始执行】")
        browser = playwright.chromium.launch(channel="msedge", headless=False,slow_mo=6000)
        context = browser.new_context()
        page = context.new_page()
        page.goto(TEST_ENV)

        if '页面标题名称' not in page.title():
            page.locator("#j25_username").click()
            page.locator("#j25_username").fill("user_name")
            page.get_by_role("textbox", name="请输入密码").click()
            page.locator("#j25_password").fill("pass_word")
            page.get_by_role("button", name="登录").click()

        time.sleep(15)
        context.close()
        browser.close()