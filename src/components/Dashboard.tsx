import React from "react"
import {useState} from "react"

/**
 * @description will prompt user to select company, then
 *              selected company will be loaded by CompanyPanel
 */
function CompanySelector() {
        return (
            <div>
                <title>Companies:</title>
            </div>
        )

}

/**
 * @description will load in selected company 
 *              onto dashboard
 */
function CompanyPanel({company}: {company: string}) {
    switch (company) {
        default: return (
            <div>
                <h1>No Company Selected</h1>
            </div>
        )

    }

}

/**
 * @description will simply load in visual and functional
 *              components, the hub where job query 
 *              parameters are selected by the user
 */
export default function Dashboard() {
    const [companyName, setCompanyName] = useState("");

    return (
        <div>
            <header>
                <h1>Welcome </h1>
                <CompanySelector/>
                <CompanyPanel company={companyName}/>
            </header>
        </div>
    )
}