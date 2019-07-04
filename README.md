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


Translation (i18n)
-------------------------------

This repo offers multiple make targets to automate the translation tasks.
First, install `requirements-test.txt`:

```bash
pip install -r requirements-test.txt
```

Each make target will be explained below:

- `extract_translations`. Use [`i18n_tool` extract](https://github.com/edx/i18n-tools) to create `.po` files based on all the tagged strings in the python and javascript code.
- `compile_translations`. Use [`i18n_tool` generate](https://github.com/edx/i18n-tools) to create `.mo` compiled files.
- `detect_changed_source_translations`. Use [`i18n_tool` changed](https://github.com/edx/i18n-tools) to identify any updated translations.
- `validate_translations`. Compile translations and check the source translations haven't changed.

If you want to add a new language:
  1. Add language to `eoc_journal/translations/config.yaml`
  2. Make sure all tagged strings have been extracted:
  ```bash
  make extract_translations
  ```
  3. Clone `en` directory to `eoc_journal/translations/<lang_code>/` for example: `eoc_journal/translations/fa_IR/`
  4. Make necessary changes to translation files headers. Make sure you have proper `Language` and `Plural-Forms` lines.
  5. When you finished your modification process, re-compile the translation messages.
  ```bash
  make compile_translations
  ```

Transifex
---------

This repo offers different make targets to automate interaction with transifex. To use these make targets first install `requirements-test.txt`.
```bash
pip install -r requirements-test.txt
```

These are the different make targets used to interact with transifex:

- `pull_translations`. Pull translations from Transifex.
- `push_translations`. Push translations to Transifex.

The transifex configuration is stored in `.tx`. For more information read [transifex's documentation](https://docs.transifex.com/client/client-configuration)
