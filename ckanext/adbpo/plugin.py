import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class ADBPoUiPlugin(plugins.SingletonPlugin):

    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('assets', 'adbpo')

    # ITemplateHelpers
    def get_helpers(self):
        return {
            'adbpo_get_groups': adbpo_get_groups,
        }


def adbpo_get_groups(limit=10):
    return toolkit.get_action('group_list')\
        (
            data_dict={
                'sort': 'package_count desc',
                'all_fields': True,
                'limit': limit
            }
        )
