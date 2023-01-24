import os

from odoo import SUPERUSER_ID, _, api, fields, models

MODULE_NAME = "defi_aliment"


def post_init_hook(cr, e):
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})

        # The path of the actual file
        path_module_generate = "addons/ERPLibre_erplibre_addons"

        short_name = MODULE_NAME.replace("_", " ").title()

        # Add code generator
        value = {
            "shortdesc": short_name,
            "name": MODULE_NAME,
            "license": "AGPL-3",
            "author": "TechnoLibre",
            "website": "https://technolibre.ca",
            "application": True,
            "enable_sync_code": True,
            "path_sync_code": path_module_generate,
        }

        # TODO HUMAN: enable your functionality to generate
        value["enable_sync_template"] = True
        value["ignore_fields"] = ""
        value["post_init_hook_show"] = False
        value["uninstall_hook_show"] = False
        value["post_init_hook_feature_code_generator"] = False
        value["uninstall_hook_feature_code_generator"] = False

        value["hook_constant_code"] = f'MODULE_NAME = "{MODULE_NAME}"'

        code_generator_id = env["code.generator.module"].create(value)

        # Add dependencies
        lst_depend_module = ["website"]
        code_generator_id.add_module_dependency(lst_depend_module)

        # Add/Update defi aliment
        model_model = "defi.aliment"
        model_name = "demo_defi_aliment"
        dct_model = {
            "description": "demo_defi_aliment",
        }
        dct_field = {
            "name": {
                "field_description": "Nom de l'aliment",
                "ttype": "char",
            },
        }
        model_defi_aliment = code_generator_id.add_update_model(
            model_model,
            model_name,
            dct_field=dct_field,
            dct_model=dct_model,
        )

        # Generate view
        # Action generate view
        wizard_view = env["code.generator.generate.views.wizard"].create(
            {
                "code_generator_id": code_generator_id.id,
                "enable_generate_all": False,
            }
        )

        wizard_view.button_generate_views()

        # Generate snippet
        value_snippet = {
            "code_generator_id": code_generator_id.id,
            "controller_feature": "helloworld",
            "model_name": "defi.aliment",
            "enable_javascript": True,
            "snippet_type": "structure",

        }
        env["code.generator.snippet"].create(value_snippet)

        # Generate module
        value = {"code_generator_ids": code_generator_id.ids}
        env["code.generator.writer"].create(value)


def uninstall_hook(cr, e):
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        code_generator_id = env["code.generator.module"].search(
            [("name", "=", MODULE_NAME)]
        )
        if code_generator_id:
            code_generator_id.unlink()
