/** @odoo-module **/

import { QuantityButtons } from "@sale/js/quantity_buttons/quantity_buttons";
import { patch } from "@web/core/utils/patch";

patch(QuantityButtons.prototype, {
    increaseQuantity() {
        this.props.setQuantity(this.props.quantity + 0.1);
    },
    decreaseQuantity() {
        this.props.setQuantity(this.props.quantity - 0.1);
    }
});
