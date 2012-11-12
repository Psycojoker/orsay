ListingView = Backbone.View.extend
    el: $("#persons")

    render: ->
        @$el.html("dummy")

    initialize: ->
        console.log "init listing view"

listing_view = new ListingView
