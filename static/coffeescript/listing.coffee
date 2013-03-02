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


PersonView = Backbone.View.extend
    tagName: "div"
    events:
        "click span": "change_watching"

    change_watching: ->
        console.log "pouet pouet"
        @person.attributes.in_recontacting_loop = not @person.attributes.in_recontacting_loop
        @person.save()
        @render()

    render: ->
        @$el.html(nunjucks.env.render('person.html', {"person": @person.toJSON()}))

    initialize: (args) ->
        @person = args.person
        @$el = $("#person_#{args.person.attributes.id}")


ListingView = Backbone.View.extend
    el: $("#persons")

    render: ->
        @$el.html(nunjucks.env.render('listing.html', {"persons": @persons.toJSON()}))
        @persons.each (person) ->
            new PersonView
                person: person

    initialize: ->
        console.log "init listing view"
        @persons = new PersonCollection

        that = this
        @persons.fetch
            success: ->
                that.render()


listing_view = new ListingView
