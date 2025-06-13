import React from "react"
import {useState} from "react"
import Adzuna from "./Adzuna"

/**
 * @description will prompt user to select company, then
 *              selected company will be loaded by CompanyPanel
 */
function CompanySelector({onSelect}: {onSelect: (company: string) => void}) {
        return (
            <div>
                <title>Companies:</title>
                <button onClick={() => onSelect("Adzuna")}>Adzuna</button>
            </div>
        )

}

/**
 * @description will load in selected company 
 *              onto dashboard
 */
function CompanyPanel({company, onBack}: {company: string, onBack: () => void}) {
    switch (company) {
        case "Adzuna":
            return (
                <div>
                    <h1>Adzuna</h1>
                    <button onClick={onBack}>Back</button>
                    <Adzuna/>
                </div>
            )

        default: return (
            <div>
                <h1>No Company Selected</h1>
                <button onClick={onBack}></button>
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
    const [companyName, setCompanyName] = useState<string | null>(null);

    return (
        <div>
            <h1>Welcome to the Dashboard</h1>
            {companyName === null ? 
            <CompanySelector onSelect={(company: string) => {setCompanyName(company)}}/> : 
            <CompanyPanel company={companyName} onBack={() => setCompanyName(null)}/>}
        </div>
    )
}