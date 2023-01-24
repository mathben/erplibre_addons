odoo.define("defi_aliment.animation", function (require) {
    "use strict";

    let sAnimation = require("website.content.snippets.animation");

    sAnimation.registry.defi_aliment = sAnimation.Class.extend({
        selector: ".o_defi_aliment",

        start: function () {
            let self = this;

            let def = this._rpc({ route: "" }).then(function (data) {
                if (data.error) {
                    return;
                }

                if (_.isEmpty(data)) {
                    return;
                }
            });

            return $.when(this._super.apply(this, arguments), def);
        },
        destroy: function () {
            this._super.apply(this, arguments);
            if (this._$loadedContent) {
            }
        },
    });
});
