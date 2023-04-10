from textual import events
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Button, Header, Footer, Static, Input, Switch
from textual.widget import Widget
from data.database import (
    create_todos_table,
    add_todo,
    get_all_todos,
    mark_todo_as_done,
    mark_todo_as_undone,
    delete_todo,
)


class ToDo(Widget):
    """A ToDo Widget"""

    def __init__(self, todo_content: str, todo_id: int, todo_done: int) -> None:
        self.todo_content = todo_content
        self.todo_id = str(todo_id)
        self.todo_done = bool(todo_done)
        super().__init__()

    def compose(
        self,
    ) -> ComposeResult:
        """Create child widgets for the app."""
        # yield Button("Done", id="done", variant="success")
        yield Horizontal(
            Static("Done: ", classes="label", id="on_label"),
            Switch(value=self.todo_done, name=self.todo_id, id="done"),
            Static(
                f"{self.todo_id}: {self.todo_content}",
                name=self.todo_id,
                id="todo_content",
            ),
            Button("Del", name=self.todo_id, id="del", variant="error"),
        )


class AddToDo(Static):
    """A ToDo Widgt"""

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Button("add", id="add")
        yield Input(placeholder="What Do you want to do?", id="input")


todos = get_all_todos()


class ToDoApp(App):
    """A Textual app to manage Todos."""

    CSS_PATH = "uis\\todos_style.css"
    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("c", "close_app", "Exit"),
    ]

    def on_mount(self) -> None:
        create_todos_table()

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        for todo in todos:
            yield ToDo(todo[0], todo[1], todo[2])
        yield AddToDo()
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

    def action_close_app(self) -> None:
        """An action to toggle dark mode."""
        self.exit()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler called when a button is pressed."""
        if event.button.id == "del":
            delete_todo(event.button.name)
            # super().refresh()
        elif event.button.id == "done":
            mark_todo_as_done(event.button.name)
        
        elif event.button.id == "add":
            add_todo()

    def on_switch_changed(self, event: Switch.Changed) -> None:
        if event.switch.value is True:
            mark_todo_as_done(event.switch.name)
        else:
            mark_todo_as_undone(event.switch.name)
