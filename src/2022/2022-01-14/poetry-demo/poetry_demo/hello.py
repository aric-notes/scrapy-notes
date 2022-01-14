# define main package
from get_set_nested_dict import get_set_nested_dict

nested_dict = {
  "club": [
    {
      "manager": {
        "last_name": "Lionel",
        "first_name": "Messi"
      }
    }
  ]
}
path = "club[0].manager.last_name"
nested_dict, manager_last_name = get_set_nested_dict(nested_dict, path, setter_value='Pulga')

print(nested_dict)

