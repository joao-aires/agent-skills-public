import "./globals.css";
export const metadata = { title: "Project Notes", description: "Verified full-stack reference" };
export default function Layout({ children }: { children: React.ReactNode }) {
  return <html lang="en"><body>{children}</body></html>;
}
