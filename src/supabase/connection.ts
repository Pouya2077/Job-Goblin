import {createClient} from "@supabase/supabase-js"
import dotenv from 'dotenv'
dotenv.config()

export default createClient((process.env.SUPA_URL as string), (process.env.ANON_KEY as string));

