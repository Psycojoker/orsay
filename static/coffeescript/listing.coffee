PersonCollection = Backbone.Collection.extend
    url: "/person/"

    initialize: ->
        console.log "New person collection"


PersonModel = Backbone.Model.extend
    initialize: ->
        console.log "New person"


ListingView = Backbone.View.extend
    el: $("#persons")

    render: ->
        @$el.html("dummy")

    initialize: ->
        console.log "init listing view"
        @persons = new PersonCollection

        that = this
        @persons.fetch
            success: ->
                that.render()


listing_view = new ListingView
