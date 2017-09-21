// register the grid base component
Vue.component('front-grid', {
    template: '#grid-template',
    props: {
        data: Array,
        columns: Array,
        filterKey: String,
        pk: String,
        url: String,
        searchText: String,
        editUrl: String,
        editMethod: String,
        deleteMethod: String
    },
    data: function () {
        var template = this;
        return {
            sortKey: template.pk,
            sort: "desc",
            pages: 1,
            currentPage: 1
        };
    },
    filters: {
        capitalize: function (str) {
            return str.charAt(0).toUpperCase() + str.slice(1);
        }
    },
    methods: {
        loadData: function () {
            var template = this;

            var xhttp = new XMLHttpRequest();
            xhttp.onreadystatechange = function() {
                if (this.readyState === 4 && this.status === 200) {
                    if(this.status === 200) {
                        var res = JSON.parse(this.responseText);
                        template.$parent.gridData = res.data;
                        template.pages = res.pages;
                    } else {
                        alert("Error");
                    }
                }
            };

            var url = this.url + "?page=" + this.currentPage;
            
            if(template.sortKey) {
                url += "&sort_by=" + template.sortKey + "&sort=" + this.sort;
            }

            if(template.searchText) {
                url += "&search=" + this.searchText;
            }

            xhttp.open("GET", url, true);
            xhttp.send();
        },
        goTo: function(p) {
            this.currentPage = p;
            this.loadData();
        },
        sortBy: function (name) {
            this.searchText = this.$el.querySelector('#grid-search-input').value;

            if(this.sortKey == name) {
                if(this.sort == 'asc')
                    this.sort = 'desc';
                else
                    this.sort = 'asc';
            } else {
                this.sortKey = name;
                this.sort = 'asc';
            }

            this.loadData();
        },
        searchBy: function(el) {
            //console.log("search by ", this.$el.querySelector('#grid-search-input'));
            this.searchText = this.$el.querySelector('#grid-search-input').value;
            this.loadData();
        }
    }
});
