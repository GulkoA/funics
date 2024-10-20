import { word_response } from "../types/api_types";

export default class API {
  static async get_word(): Promise<word_response> {
    const response = await fetch("http://127.0.0.1:5000/api/get-word");
    console.log(response);
    return response.json();
  }
}
