from h2o_wave import Q, app, handle_on, main, on, ui  # noqa F401
from h2o_wave.core import Expando


@app("/")
async def serve(q: Q):
    if not q.client.initialized:
        init_client_state(q.client)
        await render_page(q)
    else:
        await handle_on(q)


@on()
async def action_increment(q: Q):
    q.client.number = increment(q.client.number)
    await render_page(q)


def increment(number: int):
    return number + 1


def init_client_state(client_state: Expando):
    client_state.initialized = True
    client_state.number = 0


async def render_page(q: Q):
    q.page["main"] = ui.form_card(
        box="1 1 4 10",
        items=[
            ui.label(label=f"Number is: {q.client.number}", name="number"),
            ui.button(name="action_increment", label="Increment", primary=True),
        ],
    )

    await q.page.save()
