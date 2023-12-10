import libcst


class ClassRenameTransformer(libcst.CSTTransformer):

    def __init__(self, old_name, target_name):
        self._old_name = old_name
        self._target_name = target_name
        self._restore_keywords = []

    def _rename_class_name(self, original_node, renamed_node):
        if original_node.name.value == self._old_name:
            new_name = renamed_node.name.with_changes(value=self._target_name)
            return renamed_node.with_changes(name=new_name)
        else:
            return renamed_node

    def _rename_class_call_name(self, original_node, renamed_node):
        if original_node.func.value == self._old_name:
            new_func = renamed_node.func.with_changes(value=self._target_name)
            return renamed_node.with_changes(func=new_func)
        else:
            return renamed_node

    def _rename_class_arg_name(self, original_node, renamed_node):
        try:
            a = original_node.value.value
        except AttributeError as e:
            return renamed_node
        if a == self._old_name:
            new_val = renamed_node.value.with_changes(value=self._target_name)
            return renamed_node.with_changes(value=new_val)
        else:
            return renamed_node

    def _rename_func_import(self, original_node, renamed_node):
        if original_node.name.value == self._old_name:
            new_name = renamed_node.name.with_changes(value=self._target_name)
            return renamed_node.with_changes(name=new_name)
        else:
            return renamed_node

    def leave_ClassDef(self, original_node, renamed_node):
        return self._rename_class_name(original_node, renamed_node)

    def leave_Call(self, original_node, renamed_node):
        return self._rename_class_call_name(original_node, renamed_node)

    def leave_Arg(self, original_node, renamed_node):
        return self._rename_class_arg_name(original_node, renamed_node)

    def leave_Assign(self, original_node, renamed_node):
        return self._rename_class_arg_name(original_node, renamed_node)

    def leave_ImportAlias(self, original_node, renamed_node):
        return self._rename_func_import(original_node, renamed_node)


def rename_class(source_code: str, old_name: str, target_name: str) -> str:
    rename_transformer = ClassRenameTransformer(old_name, target_name)
    original_tree = libcst.parse_module(source_code)
    print(original_tree)
    renamed_tree = original_tree.visit(rename_transformer)
    return renamed_tree.code


