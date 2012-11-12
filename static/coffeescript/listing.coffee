if !nunjucks.env
    nunjucks.env = new nunjucks.Environment(new nunjucks.HttpLoader('/static/nunjucks'))
    nunjucks.env.addFilter('markdown', (str, count) -> markdown.toHTML(str))

render_template = nunjucks.env.render

PersonCollection = Backbone.Collection.extend
    url: "/person/"

    initialize: ->
        console.log "New person collection"


PersonModel = Backbone.Model.extend
    url: -> if @id? then "/person/#{@id}/" else "/person/"


ListingView = Backbone.View.extend
    el: $("#persons")

    render: ->
        @$el.html(nunjucks.env.render('listing.html', {"persons": @persons.toJSON()}))

    initialize: ->
        console.log "init listing view"
        @persons = new PersonCollection

        that = this
        @persons.fetch
            success: ->
                that.render()


listing_view = new ListingView
