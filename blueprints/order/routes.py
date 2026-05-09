"""
blueprints/order/routes.py
Here i will make the order related thigns and blueprint obj
"""

from flask import Blueprint, render_template

from flask_login import login_required  # type: ignore

order_bp = Blueprint(
    name="order_bp",
    import_name=__name__,
    template_folder="templates",
)


@order_bp.route("/orders")
@login_required
def order():
    """
    i will need to fully modefy this, now i am making for page complition
    Demo order history page (temporary data)
    Later will connect to DB
    """

    demo_orders = [
        {
            "id": 101,
            "date": "2026-05-01",
            "status": "Delivered",
            "total": 45000,
            "items": 3,
        },
        {
            "id": 102,
            "date": "2026-05-10",
            "status": "Processing",
            "total": 12000,
            "items": 1,
        },
        {
            "id": 103,
            "date": "2026-05-15",
            "status": "Shipped",
            "total": 7800,
            "items": 2,
        },
    ]

    return render_template(
        "order/order.html",
        orders=demo_orders,
    )
