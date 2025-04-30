import {createClient} from "@supabase/supabase-js"

const supabase = createClient((process.env.SUPA_URL as string), (process.env.ANON_KEY as string));

export default supabase;