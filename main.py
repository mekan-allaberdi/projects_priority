import json


def solution():
    with open('source_file_2.json') as json_file:
        project_list = json.load(json_file)

    project_list.sort(key=lambda x: x['priority'])

    manager_dict = {}
    watcher_dict = {}

    for project in project_list:
        name = project['name']
        managers = project['managers']
        watchers = project['watchers']

        for manager in managers:
            if manager_dict.get(manager, None) is None:
                manager_dict[manager] = []
            manager_dict[manager].append(name)

        for watcher in watchers:
            if watcher_dict.get(watcher, None) is None:
                watcher_dict[watcher] = []
            watcher_dict[watcher].append(name)

    with open('watchers.json', 'w') as outfile:
        outfile.write(json.dumps(watcher_dict, indent=4))

    with open('managers.json', 'w') as outfile:
        outfile.write(json.dumps(manager_dict, indent=4))


if __name__ == '__main__':
    solution()
