/**
 * ARGON public config. One file. Every page reads this object.
 *
 * LIVE PAYMENT LINKS ARE BLANK ON PURPOSE.
 * Karl must paste live-mode Payment Links (buy.stripe.com links that are NOT
 * /test_ links) into paymentLinks.live, then set mode to "live".
 * The sandbox links below are Stripe test mode. They cannot take a real card.
 *
 * Only public Payment Links belong here.
 * Never put Stripe secret keys (sk_live_ / sk_test_) or restricted keys (rk_) in this file.
 *
 * leadWebhookUrl stays empty. Do not commit an Apps Script URL.
 * Rotate that deployment if a URL was committed before. Store the new one
 * outside the repo, or accept that any value placed here is public.
 */
(function () {
  var live = {
    core97: "",
    bundle394: "",
    upsell297: ""
  };

  var sandbox = {
    core97: "https://buy.stripe.com/test_dRm14gfqDc9Nae1fBC5AQ00",
    bundle394: "https://buy.stripe.com/test_00waEQdiv8XBgCpahi5AQ01",
    // The old vault-access placeholder returned HTTP 403. Left blank so the
    // page does not send buyers there. Karl pastes a real link under live.upsell297.
    upsell297: ""
  };

  var config = {
    // "sandbox" until Karl supplies live links and switches this to "live".
    mode: "sandbox",
    prices: {
      coreUsd: 97,
      bumpUsd: 297
    },
    copy: {
      productName: "The Blueprint",
      productDescription: "The practical guide to building your own AI-driven revenue engine.",
      bumpName: "Build kit",
      bumpDescription: "The working funnel, controller, and affiliate bridges.",
      bundleName: "The Blueprint + Build Kit"
    },
    paymentLinks: {
      live: live,
      sandbox: sandbox
    },
    leadWebhookUrl: "",

    activeLinks: function () {
      return this.mode === "live" ? this.paymentLinks.live : this.paymentLinks.sandbox;
    },

    /**
     * Public Payment Link for a product key.
     * Appends ?prefilled_email= when the visitor already typed an email.
     * Returns "" when that link is not configured.
     */
    checkoutUrl: function (key, email) {
      var url = ((this.activeLinks()[key]) || "").trim();
      if (!url) return "";
      if (!email) return url;
      var joiner = url.indexOf("?") === -1 ? "?" : "&";
      return url + joiner + "prefilled_email=" + encodeURIComponent(email);
    },

    primaryCta: function () {
      return "Get the Blueprint — $" + this.prices.coreUsd;
    }
  };

  window.ARGON_CONFIG = config;
})();
