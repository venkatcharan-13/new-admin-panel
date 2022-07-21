endpoint = 'api/List_of_companies/'


$.ajax({
    method: "GET",
    url: endpoint,
    success: function(data) {
        console.log("Success Admin");

        all_companies(data)

    },
    error: function(error_data) {
        console.log("Error1");
        console.log(error_data);
    }
})



function all_companies(data) {
    var all_companies = 1;

    data.forEach((for_each_item) => {
        var company = ` <tr><td> </td>
        <td><a href="api/${for_each_item.company_id}">${for_each_item.company_id}</a></td>
        <td width=80px><a href="api/${for_each_item.company_id}">${for_each_item.company_name}</a></td>
    </tr>`
        document.getElementById('AllCompany').insertAdjacentHTML('beforeend', company)
        all_companies++;

    })

}