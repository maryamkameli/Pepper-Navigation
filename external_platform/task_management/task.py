TASK_NO = 1


class Task:
    def __init__(self, type, priority=3, class_type='', label='', value=''):
        global TASK_NO

        self.id = TASK_NO
        self.type = type
        self.priority = priority
        self.class_type = class_type
        self.label = label
        self.value = value
        self.done = False

        TASK_NO += 1

    def is_done(self):
        return self.done

    def stringify(self):
        return '\n%s: \tID: %d \tPrior: %d \tClass: %s \tLabel: %s \tValue: %s' % \
            ((self.type,)+(self.id,)+(self.priority,)+(self.class_type,)+(self.label,)+(self.value,))

    def __str__(self):
        return self.stringify()

    def __repr__(self):
        return self.__str__()
