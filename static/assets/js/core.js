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

                var afterSuccessType = base.el.form.attr('data-succ-type');
                var afterSuccessUrl = base.el.form.attr('data-succ-url');
                var afterSuccessWait = base.el.form.attr('data-succ-wait');

                if (typeof afterSuccessType !== typeof undefined && afterSuccessType !== false) {
                    base.actions.after_success.type = afterSuccessType;
                }
                if (typeof afterSuccessUrl !== typeof undefined && afterSuccessUrl !== false) {
                    base.actions.after_success.url = afterSuccessUrl;
                }
                if (typeof afterSuccessWait !== typeof undefined && afterSuccessWait !== false) {
                    base.actions.after_success.wait = afterSuccessWait;
                }

            }
        },
        submit : function(){
            base.el.form.on("submit", base.handler);
        },
        handler: function(event) {
            event.preventDefault();
            $(this).find("button[type='submit']").attr('disabled', 'disabled');
            $(this).find("button[type='submit']").addClass("btn-loading");
            require(['pace'], function(Pace) {
                Pace.track(function(){
                    $.post(base.el.form.attr('action'), base.data(), function( response, textStatus, jqXHR ){
                        if( jqXHR.status == 200 && textStatus == 'success' ) {
                            if( response.status == "success" ){
                                base.success(response.messages);
                            }else{
                                base.error(response.messages);
                            }
                        }
                    }, 'json');
                });
            });
        },
        data : function(){
            var inputs = {};
            base.el.form.serializeArray().map(function(item, index) {
                inputs[item.name] = item.value;
            });
            return inputs;
        },
        success : function(messages){
            for(var messageObj of messages) {
                require(['toastr'], function(toastr) {
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
                base.el.submitButt.removeAttr('disabled');
                base.el.submitButt.removeClass('btn-loading');
            }
        },
        error : function(messages){
            base.el.submitButt.removeAttr('disabled');
            base.el.submitButt.removeClass('btn-loading');
            require(['toastr'], function(toastr) {
                toastr.clear();
            });
            for(var messageObj of messages) {
                require(['toastr'], function(toastr) {
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

    require(['jscookie'], function(Cookies) {
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