+++
title = 'Insert File Shortcode'
date = 2023-12-21T04:12:58-06:00
draft = false
tags = ['hugo']
+++


## Insert another file into a content file

Note to self:

Here's an example [shortcode](https://gohugo.io/content-management/shortcodes/) to insert the contents of one file into another.

In **/layouts/shortcodes/** create a file with the code

>{{ readFile "file-to-insert" }}

Name the shortcut file with the .html extension.

In the body of the content file call the shortcode with the code

> {{%/* myshortcode */%}}
 
See more at the Hugo documentation website [here](https://gohugo.io/content-management/shortcodes/).