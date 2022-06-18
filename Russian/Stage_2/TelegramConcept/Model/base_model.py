class BaseScreenModel:
    """
    Реализует базовый класс модели для всех экранов (представлений) приложения.
    """

    _observers = []  # список наблюдателей (объектов представлений)

    def __init__(self, database=None):
        self.database = database

    def add_observer(self, observer) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer) -> None:
        self._observers.remove(observer)

    def notify_observers(self, name_screen: str) -> None:
        """
        Метод, который будет вызываться при изменении данных модели.

        :param name_screen:
            имя представления, для которого должен быть вызван метод
            :meth:`model_is_changed`.
        """

        # Оповещение всех наблюдателей об изменении данных модели.
        for observer in self._observers:
            if observer.name == name_screen:
                observer.model_is_changed()
                break
