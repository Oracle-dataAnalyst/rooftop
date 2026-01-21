import { request } from "./http";

export const postChat = (message: string) => {
  return request("/chat", {
    method: "POST",
    body: JSON.stringify({ message }),
  });
};
