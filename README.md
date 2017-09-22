# vuejs-simple-datatable
Example of a table built with vuejs which has searching/sorting/pagination for data got by ajax calls

# Components
* Backend: Flask (python 3.5.3)
* Frontend: Bootstrap 3.3.7 and Vuejs 2.4.2

# Use
* This component is created as a generic template, so it can be used as a generic data table. 
  The way to create the html tag is like:
```html
<div id="clubs-grid-container" class="grid-container">
    <front-grid
            :pk="pk"
            :search-text="searchText"
            :url="listUrl"
            :data="gridData"
            :columns="gridColumns"
            :filter-key="searchQuery"
            :edit-url="editUrl">
    </front-grid>
</div>
```
And the javascript code would be:
```javascript
// bootstrap the container
var listContainer = new Vue({
    el: '#clubs-grid-container',
    data: {
        pk: "key",
        searchText: "",
        listUrl: "/list",
        editUrl: "/edit/<pk>",
        searchQuery: '',
        gridColumns: [
            { name: 'key', label: 'Key'},
            { name: 'code', label: 'Code' },
            { name: 'name', label: 'Name', sort: 'asc', edit: true }
        ],
        gridData: []
    }
});
listContainer.$children[0].loadData();
```
Just make sure to include the content of templates/templates.html and static/js/vue-components.js before the previous js code.

# Notes
* I'm using Flask (python 3) just as a backend system in order to get data by ajax, but the datatable is independent of your backend implementation. Additionally you can check the pagination/sorting/searching logic in backend. Instead of using a database, I'm using a simple json file with a list of football clubs.
