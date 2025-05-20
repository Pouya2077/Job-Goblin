import supabase from "./connection"

export async function signUpWithPassword(email: string, password: string, name: string) {
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

export async function signInWithPassword(email: string, password: string) {
    return supabase.auth.signInWithPassword({
        email: email, 
        password: password,
    })
}
