Virtual Reality XBlock
======================

This XBlock embeds Virtual Reality videos into a course.

Install
-------

See [edX Installing an XBlock](http://edx.readthedocs.io/projects/edx-installing-configuring-and-running/en/latest/configuration/install_xblock.html?highlight=install%20xblock)
for details on how to install this XBlock on your Open edX instance.

```python
pip install "git+https://github.com/open-craft/xblock-virtualreality@master#egg=xblock-virtualreality"
```

Usage
-----

To enable the `virtualreality` xblock in your course:

1. In Studio, go to `Settings > Advanced Settings`.
1. Locate the `Advanced Module List` field, and add `"virtualreality"` to that list.
1. Add a Unit to your course, and click on the `Advanced` button to add a `Vimeo` component.
1. Click `Edit` to add your Video URL.
1. Click Save to add the video to your course.
