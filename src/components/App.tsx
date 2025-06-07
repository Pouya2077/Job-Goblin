import * as Query from '../adzuna/query'
import * as Parse from '../adzuna/parse'
import * as Auth from '../supabase/auth'
import React, {useState, useEffect} from 'react'
import {Job} from "../types"
import { Sign } from 'crypto'

export default function App() {

    return (
        <div>
            <header>
                <h1>Welcome to Job Goblin!</h1>
            </header>
            
            <div>
                <button>
                    Login
                </button>
                <button>
                    SignUp
                </button>
            </div>
        </div>
    )

}


