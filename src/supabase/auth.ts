import supabase from "./connection.js"

export async function signUp(email: string, password: string, name: string) {
    return supabase.auth.signUp({
        email: email, 
        password: password, 
        options: {
            data: {
                display_name: name,
            }
        }
    })
}

export async function passwordSignIn(email: string, password: string) {
    return supabase.auth.signInWithPassword({
        email: email, 
        password: password,
    })
}
