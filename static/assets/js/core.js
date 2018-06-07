require(['jscookie', 'toastr', 'pace']);

var kevin_app = kevin_app || {};


/**
 * Form to Enpoint Connect
 */
kevin_app.endpoint_connect = (function (window, document, $) {

    'use strict';

    var base = {

        el: {
            form : $("form._endpoint_connect"),
            submitButt : $("form._endpoint_connect button[type='submit']"),
        },
        actions: {
            after_success: {
                type: false,
                url: false,
                wait: false
            }

        },
        init: function(){
            if( base.el.form.length ){
                base.submit();
            }
        },
        submit : function(){
            base.el.form.on("submit", base.handler);
        },
        handler: function(event) {
            event.preventDefault();

            base.actions.after_success.type = false;
            base.actions.after_success.url = false;
            base.actions.after_success.wait = false;

            var _form = $(this);
            var _button = $(this).find("button[type='submit']");

            var afterSuccessType = _form.attr('data-succ-type');
            var afterSuccessUrl = _form.attr('data-succ-url');
            var afterSuccessWait = _form.attr('data-succ-wait');

            if (typeof afterSuccessType !== typeof undefined && afterSuccessType !== false) {
                base.actions.after_success.type = afterSuccessType;
            }
            if (typeof afterSuccessUrl !== typeof undefined && afterSuccessUrl !== false) {
                base.actions.after_success.url = afterSuccessUrl;
            }
            if (typeof afterSuccessWait !== typeof undefined && afterSuccessWait !== false) {
                base.actions.after_success.wait = afterSuccessWait;
            }

            _button.attr('disabled', 'disabled');
            _button.addClass("btn-loading");
            require(['pace'], function(Pace) {
                Pace.track(function(){
                    $.post(_form.attr('action'), base.data(_form, _button), function( response, textStatus, jqXHR ){
                        if( jqXHR.status == 200 && textStatus == 'success' ) {
                            if( response.status == "success" ){
                                base.success(response.messages, _form, _button);
                            }else{
                                base.error(response.messages, _form, _button);
                            }
                        }
                    }, 'json');
                });
            });
        },
        data : function(form, button){
            var inputs = {};
            form.serializeArray().map(function(item, index) {
                inputs[item.name] = item.value;
            });
            return inputs;
        },
        success : function(messages, form, button){
            for(var messageObj of messages) {
                require(['toastr'], function(toastr) {
                    toastr.clear();
                    toastr.success(messageObj.message);
                });
                break;
            }
            if( base.actions.after_success.type == "reload" ){
                if( base.actions.after_success.wait != false ){
                    setTimeout(function(){
                        location.reload();
                    }, base.actions.after_success.wait);
                }else{
                    location.reload();
                }
            }
            if( base.actions.after_success.type == "redirect" ){
                if( base.actions.after_success.wait != false ){
                    setTimeout(function(){
                        location.href = base.actions.after_success.url;
                    }, base.actions.after_success.wait);
                }else{
                    location.href = base.actions.after_success.url;
                }
            }

            if( base.actions.after_success.type == "nothing" ){
                button.removeAttr('disabled');
                button.removeClass('btn-loading');
            }
            if( base.actions.after_success.type == "reset" ){
                form[0].reset();
                button.removeAttr('disabled');
                button.removeClass('btn-loading');
            }
        },
        error : function(messages, form, button){
            button.removeAttr('disabled');
            button.removeClass('btn-loading');
            for(var messageObj of messages) {
                require(['toastr'], function(toastr) {
                    toastr.clear();
                    toastr.error(messageObj.message);
                });
                break;
            }
        }
    };

   return {
        init: base.init
    };

})(window, document, jQuery);



kevin_app.profile = (function (window, document, $) {

    'use strict';

    var base = {

        el: {
            update_access_token : $("#profile_update_access_token"),
            update_refresh_token : $("#profile_update_refresh_token"),
        },
        init: function(){
            if( base.el.update_access_token.length ){
                base.el.update_access_token.find("button").on("click", function(event){
                    event.preventDefault();

                    if( !confirm(_i18n.confirm_msg) ){
                        return false;
                    }

                    var _self = $(this);
                    _self.attr('disabled', 'disabled');
                    _self.addClass("btn-loading");

                    require(['pace', 'jscookie'], function(Pace, Cookies) {
                        Pace.track(function(){
                            $.post(_self.attr('data-url'), {
                                "action": _self.attr('data-action'),
                                "token": base.el.update_access_token.find("input").val(),
                                "csrfmiddlewaretoken": Cookies.get('csrftoken')
                            }, function( response, textStatus, jqXHR ){
                                if( jqXHR.status == 200 && textStatus == 'success' ) {
                                    if( response.status == "success" ){
                                        base.success(response.messages);
                                        base.el.update_access_token.find("input").val(response.payload.token);
                                        _self.removeAttr('disabled');
                                        _self.removeClass("btn-loading");
                                    }else{
                                        base.error(response.messages);
                                        _self.removeAttr('disabled');
                                        _self.removeClass("btn-loading");
                                    }
                                }
                            }, 'json');
                        });
                    });
                })
            }
            if( base.el.update_refresh_token.length ){
                base.el.update_refresh_token.find("button").on("click", function(event){
                    event.preventDefault();

                    if( !confirm(_i18n.confirm_msg) ){
                        return false;
                    }

                    var _self = $(this);
                    _self.attr('disabled', 'disabled');
                    _self.addClass("btn-loading");

                    require(['pace', 'jscookie'], function(Pace, Cookies) {
                        Pace.track(function(){
                            $.post(_self.attr('data-url'), {
                                "action": _self.attr('data-action'),
                                "token": base.el.update_refresh_token.find("input").val(),
                                "csrfmiddlewaretoken": Cookies.get('csrftoken')
                            }, function( response, textStatus, jqXHR ){
                                if( jqXHR.status == 200 && textStatus == 'success' ) {
                                    if( response.status == "success" ){
                                        base.success(response.messages);
                                        base.el.update_refresh_token.find("input").val(response.payload.token);
                                        _self.removeAttr('disabled');
                                        _self.removeClass("btn-loading");
                                    }else{
                                        base.error(response.messages);
                                        _self.removeAttr('disabled');
                                        _self.removeClass("btn-loading");
                                    }
                                }
                            }, 'json');
                        });
                    });
                })
            }
        },
        success : function(messages){
            for(var messageObj of messages) {
                require(['toastr'], function(toastr) {
                    toastr.clear();
                    toastr.success(messageObj.message);
                });
                break;
            }
        },
        error : function(messages){
            for(var messageObj of messages) {
                require(['toastr'], function(toastr) {
                    toastr.clear();
                    toastr.error(messageObj.message);
                });
                break;
            }
        }
    };

   return {
        init: base.init
    };

})(window, document, jQuery);


/**
 * Namespace Endpoints
 */
kevin_app.namespace = (function (window, document, $) {

    'use strict';

    var base = {

        el: {
            namespaceName : $('form#namespace_create input[name="name"]'),
            namespaceSlug : $('form#namespace_create input[name="slug"]'),
            namespaceDelete: $('a.delete_namespace')
        },
        init: function(){
            if( base.el.namespaceName.length ){
                base.el.namespaceName.on("change", base.namespaceNameChange);
            }
            if( base.el.namespaceDelete.length ){
                base.el.namespaceDelete.on("click", base.deleteNamespace);
            }
        },

        deleteNamespace: function(event) {
            event.preventDefault();

            if( !confirm(_i18n.confirm_msg) ){
                return false;
            }

            var _self = $(this);
            _self.attr('disabled', 'disabled');
            require(['pace', 'jscookie'], function(Pace, Cookies) {
                Pace.track(function(){
                    $.ajax({
                      method: "DELETE",
                      url: _self.attr('data-url') + "?csrfmiddlewaretoken=" + Cookies.get('csrftoken'),
                      data: { "csrfmiddlewaretoken": Cookies.get('csrftoken') }
                    }).done(function( response ) {
                        if( response.status == "success" ){
                            base.success(response.messages);
                            _self.closest("tr").remove();
                        }else{
                            base.error(response.messages);
                        }
                    });
                });
            });
        },

        namespaceNameChange: function(event) {
            event.preventDefault();
            base.el.namespaceSlug.val(base.slugify(base.el.namespaceName.val()))
        },
        slugify: function(text) {
          return text.toString().toLowerCase()
            .replace(/\s+/g, '-')           // Replace spaces with -
            .replace(/[^\w\-]+/g, '')       // Remove all non-word chars
            .replace(/\-\-+/g, '-')         // Replace multiple - with single -
            .replace(/^-+/, '')             // Trim - from start of text
            .replace(/-+$/, '');            // Trim - from end of text
        },
        success : function(messages){
            for(var messageObj of messages) {
                require(['toastr'], function(toastr) {
                    toastr.clear();
                    toastr.success(messageObj.message);
                });
                break;
            }
        },
        error : function(messages){
            for(var messageObj of messages) {
                require(['toastr'], function(toastr) {
                    toastr.clear();
                    toastr.error(messageObj.message);
                });
                break;
            }
        }
    };

   return {
        init: base.init
    };

})(window, document, jQuery);



/**
 * Endpoint Endpoints
 */
kevin_app.endpoint = (function (window, document, $) {

    'use strict';

    var base = {

        el: {
            endpointDelete: $('a.delete_endpoint'),
            addHeaderRuleButton: $('a#add_header_rule'),
            headerRules: $('tbody#header_rules'),
            submitButton: $('form#endpoint_add')
        },
        init: function(){
            if( base.el.endpointDelete.length ){
                base.el.endpointDelete.on("click", base.deleteEndpoint);
            }
            if( base.el.addHeaderRuleButton.length ){
                base.el.addHeaderRuleButton.on("click", base.addHeaderRule);
            }
            if( base.el.headerRules.length ){
                base.el.headerRules.on("click", "a.remove_header_rule", base.removeHeaderRule);
            }
            if( base.el.submitButton.length ){
                base.el.submitButton.on("click", base.submitButtonPreAction);
            }
        },
        submitButtonPreAction: function(event) {
            var max = $("tbody#header_rules tr").length;
            var value = "[";
            for (var i = 2; i <= max; i++) {
                if ($('[name="header_key[' + i + ']"]').length && $('[name="header_condition[' + i + ']"]').length && $('[name="header_value[' + i + ']"]').length ){
                    value += '{"key":"' + $('[name="header_key[' + i + ']"]').val() + '","condition":"' + $('[name="header_condition[' + i + ']"]').val() + '","value":"' + $('[name="header_value[' + i + ']"]').val() + '"},';
                }
            }
            value = value.replace(/,$/, '');
            value += "]";
            $("input[name='headers_rules']").val(value);
        },
        removeHeaderRule: function(event) {
            event.preventDefault();

            if( !confirm(_i18n.confirm_msg) ){
                return false;
            }
            var _self = $(this);
            _self.closest("tr").remove();
        },
        addHeaderRule: function(event) {
            event.preventDefault();
            var _self = $(this);
            var item = $("tr#header_rule_item").clone().removeAttr('id').show();
            item.html(item.html().replace(/\[iii\]/g,"["+ ($("tbody#header_rules tr").length + 1) + "]"));
            item.appendTo('tbody#header_rules');
        },

        deleteEndpoint: function(event) {
            event.preventDefault();

            if( !confirm(_i18n.confirm_msg) ){
                return false;
            }

            var _self = $(this);
            _self.attr('disabled', 'disabled');
            require(['pace', 'jscookie'], function(Pace, Cookies) {
                Pace.track(function(){
                    $.ajax({
                      method: "DELETE",
                      url: _self.attr('data-url') + "?csrfmiddlewaretoken=" + Cookies.get('csrftoken'),
                      data: { "csrfmiddlewaretoken": Cookies.get('csrftoken') }
                    }).done(function( response ) {
                        if( response.status == "success" ){
                            base.success(response.messages);
                            _self.closest("tr").remove();
                        }else{
                            base.error(response.messages);
                        }
                    });
                });
            });
        },
        success : function(messages){
            for(var messageObj of messages) {
                require(['toastr'], function(toastr) {
                    toastr.clear();
                    toastr.success(messageObj.message);
                });
                break;
            }
        },
        error : function(messages){
            for(var messageObj of messages) {
                require(['toastr'], function(toastr) {
                    toastr.clear();
                    toastr.error(messageObj.message);
                });
                break;
            }
        }
    };

   return {
        init: base.init
    };

})(window, document, jQuery);

/**
 *
 */
let hexToRgba = function(hex, opacity) {
    let result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    let rgb = result ? {
        r: parseInt(result[1], 16),
        g: parseInt(result[2], 16),
        b: parseInt(result[3], 16)
    } : null;
    return 'rgba(' + rgb.r + ', ' + rgb.g + ', ' + rgb.b + ', ' + opacity + ')';
};

/**
 *
 */
$(document).ready(function() {




    $(document).ajaxStart(function() {
        require(['pace'], function(Pace) {
            Pace.restart();
        });
    });

    /** Constant div card */
    const DIV_CARD = 'div.card';

    kevin_app.endpoint_connect.init();
    kevin_app.profile.init();
    kevin_app.namespace.init();
    kevin_app.endpoint.init();

    require(['jscookie'], function(Cookies) {
        $.ajaxSetup({
            headers:
            { 'X-CSRFToken': Cookies.get('csrftoken') }
        });
        console.log(Cookies.get('csrftoken'))
    })

    /** Initialize tooltips */
    $('[data-toggle="tooltip"]').tooltip();

    /** Initialize popovers */
    $('[data-toggle="popover"]').popover({
        html: true
    });

    /** Function for remove card */
    $('[data-toggle="card-remove"]').on('click', function(e) {
        let $card = $(this).closest(DIV_CARD);
        $card.remove();
        e.preventDefault();
        return false;
    });

    /** Function for collapse card */
    $('[data-toggle="card-collapse"]').on('click', function(e) {
        let $card = $(this).closest(DIV_CARD);
        $card.toggleClass('card-collapsed');
        e.preventDefault();
        return false;
    });

    /** Function for fullscreen card */
    $('[data-toggle="card-fullscreen"]').on('click', function(e) {
        let $card = $(this).closest(DIV_CARD);
        $card.toggleClass('card-fullscreen').removeClass('card-collapsed');
        e.preventDefault();
        return false;
    });

    /**  */
    if ($('[data-sparkline]').length) {
        let generateSparkline = function($elem, data, params) {
            $elem.sparkline(data, {
                type: $elem.attr('data-sparkline-type'),
                height: '100%',
                barColor: params.color,
                lineColor: params.color,
                fillColor: 'transparent',
                spotColor: params.color,
                spotRadius: 0,
                lineWidth: 2,
                highlightColor: hexToRgba(params.color, .6),
                highlightLineColor: '#666',
                defaultPixelsPerValue: 5
            });
        }
        require(['sparkline'], function() {
            $('[data-sparkline]').each(function() {
                let $chart = $(this);
                generateSparkline($chart, JSON.parse($chart.attr('data-sparkline')), {
                    color: $chart.attr('data-sparkline-color')
                });
            });
        });
    }

    /**  */
    if ($('.chart-circle').length) {
        require(['circle-progress'], function() {
            $('.chart-circle').each(function() {
                let $this = $(this);

                $this.circleProgress({
                    fill: {
                        color: tabler.colors[$this.attr('data-color')] || tabler.colors.blue
                    },
                    size: $this.height(),
                    startAngle: -Math.PI / 4 * 2,
                    emptyFill: '#F4F4F4',
                    lineCap: 'round'
                });
            });
        });
    }
});